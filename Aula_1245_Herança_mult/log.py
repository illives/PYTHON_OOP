class LogMixin:

    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as f:
            f.write(f'{msg}\n')
    
    def log_info(self,msg):
        self.write(f'INFO: {msg}')

    def log_erro(self,msg):
        self.write(f'ERRO: {msg}')
