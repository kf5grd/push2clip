import click
import json
import os
import requests

def simplepush(key, title='', message='', event=''):
    r = requests.post('https://api.simplepush.io/send', data = { 'key' : key, 'title' : title, 'msg' : message, 'event' : event })
    if r.json()['status'] == "OK":
        return True
    return False

@click.group(invoke_without_command=True)
@click.pass_context
@click.option('-k', '--key', help="Simplepush key to send to")
@click.option('-c', '--config', default='./config.json', help="Path to config file", type=click.Path(exists=False, file_okay=True, dir_okay=False, resolve_path=True))
@click.option('-m', '--message', help="Message to push to clipboard. Default is stdin")
@click.option('-V', '--verbose', is_flag=True, help="Display information after successful push")
def cli(ctx, message, key, config, verbose):
    """Use simplepush and tasker to push text to remote phone's clipboard."""

    if ctx.invoked_subcommand is None:
        if not os.path.exists(config):
            click.echo("Config file: {}".format(config))
            click.echo("Config file does not exist. Please choose a different file, or initialize with push2clip init <key>")
            quit()

        with open(config, 'r') as f:
            conf = json.load(f)
            f.close()

        if not key:
            if not conf['key']:
                print("Error: Simplepush key is missing. Unable to send push.")
                quit()
            key = conf['key']

        if not message:
            message = click.get_text_stream('stdin').read()

        event = conf.get("event", '')
        title = conf.get("title", '')
    
        sp = simplepush(key, event=event, title=title, message=message) 
        if not sp:
            click.echo("An error was encountered while pushing message.")
        else:
            if verbose:
                click.echo("Push sent successfully.")
                click.echo("Key: {}".format(key))
                click.echo("Event: {}".format(event))
                click.echo("Title: {}".format(title))
                click.echo("Message: {}".format(message))

@cli.command()
@click.option('-c', '--config', default='./config.json', help="Path to config file", type=click.Path(exists=False, file_okay=True, dir_okay=False, resolve_path=True))
@click.option('-t', '--title', default='clip', help="Simplepush title field")
@click.option('-e', '--event', default='tasker', help="Simplepush event field")
@click.argument('key', nargs=1)
def init(config, title, event, key):
    conf = {
            'title' : title,
            'event' : event,
            'key' : key,
    }
    try:
        with open(config, 'w+') as f:
            json.dump(conf, f)
            f.close()
        #json.dump(conf, config)
        click.echo("Config file initialized.")
    except:
        click.echo("Error writing config file.")

