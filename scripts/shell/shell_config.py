import os


class ShellConfig:
    # TODO
    pass


class AiobotConfig:
    token = ''

    @staticmethod
    def get_token():
        if AiobotConfig.token == '':
            from scripts.config.env_loader import load_env

            load_env()
            AiobotConfig.token = os.environ.get('TOKEN')
        return AiobotConfig.token
