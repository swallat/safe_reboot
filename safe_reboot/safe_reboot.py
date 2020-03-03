"""Console script for safe_reboot."""
import subprocess
import sys
import click
import shlex


def get_all_user_tty_mac():
    cmd = shlex.split("ps axo user,tty")
    out = subprocess.check_output(cmd).decode("utf-8")
    lines = out.strip().split('\n')
    lines = [x.split() for x in lines[1:]]
    users = dict()
    for line in lines:
        # Only consider non root and non system user ttys
        if line[0].startswith("_") or line[0] == 'root' or line[1] == "??":
            continue
        else:
            if line[0] not in users.keys():
                users[line[0]] = set()
            users[line[0]].add(line[1])
    return users



def get_all_user_tty_linux():
    cmd = shlex.split("ps axno user,tty")

def get_all_user_tty():
    get_all_user_tty_mac()



@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option('--force', '-f', help="Force reboot", default=False, is_flag=True)
@click.option('--show', '-s', help="Only show active users", default=False, is_flag=True)
def main(force, show):
    """Console script for safe_reboot."""
    click.echo("Replace this message by putting your code into "
               "safe_reboot.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")

    get_all_user_tty()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
