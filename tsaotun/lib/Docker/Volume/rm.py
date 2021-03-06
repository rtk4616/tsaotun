"""This module contains `docker volume rm` class"""

from docker.errors import APIError

from .command import Command


class Rm(Command):
    """This class implements `docker volume rm` command"""

    name = "volume rm"
    require = []

    def __init__(self):
        Command.__init__(self)
        self.settings[self.name] = None

    def eval_command(self, args):
        try:
            Ids = []
            volumes = args["volumes"]
            del args["volumes"]
            for Id in volumes:
                Ids.append(Id)
                self.client.remove_volume(Id)
            self.settings[self.name] = '\n'.join(Ids)
        except APIError as e:
            raise e

    def final(self):
        return self.settings[self.name]
