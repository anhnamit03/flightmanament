from FlightManament.Service.Interface.ILoginService import ILoginService


class LoginService(ILoginService):
    def login_with_google(self, username: str, password: str):
        print("Hello")
