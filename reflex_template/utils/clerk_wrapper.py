import reflex as rx
import os
import json

class ClerkProvider(rx.Component):
    library = "@clerk/clerk-react"
    tag = "ClerkProvider"
    publishable_key: rx.Var[str] = os.getenv("CLERK_PUBLISHABLE_KEY")
    
class SignedIn(rx.Component):
    library = "@clerk/clerk-react"
    tag = "SignedIn"

class SignedOut(rx.Component):
    library = "@clerk/clerk-react"
    tag = "SignedOut"

class SignIn(rx.Component):
    library = "@clerk/clerk-react"
    tag = "SignIn"

class UserButton(rx.Component):
    library = "@clerk/clerk-react"
    tag = "UserButton"
    
class SignInButton(rx.Component):
    library = "@clerk/clerk-react"
    tag = "SignInButton"

class SignUpButton(rx.Component):
    library = "@clerk/clerk-react"
    tag = "SignUpButton"

class SignOutButton(rx.Component):
    library = "@clerk/clerk-react"
    tag = "SignOutButton"

class UseUser(rx.Component):
    library = "@clerk/clerk-react"
    tag = "useUser"


clerk_provider = ClerkProvider.create
signed_in = SignedIn.create
signed_out = SignedOut.create
sign_in = SignIn.create
user_button = UserButton.create

sign_in_button = SignInButton.create
sign_up_button = SignUpButton.create
sign_out_button = SignOutButton.create
use_user = UseUser.create


class ClerkUserState(rx.State):
    name: str = ""
    user_signed_in: bool = False

    def update_user_info(self, user_info_str):
        print(f"User Info: {user_info_str}")
        user_info = json.loads(user_info_str)
        self.name = user_info.get('name', '')
        self.user_signed_in = user_info.get('user_signed_in', False)
        return rx.text("User Info Updated!")

    def print_user_info(self):
        print(f"Name: {self.name}, User Signed In: {self.user_signed_in}")
        

class ClerkUser(rx.Fragment):
    def _get_imports(self) -> rx.utils.imports.ImportDict:
        return rx.utils.imports.merge_imports(
            super()._get_imports(),
            {
                "@clerk/clerk-react": {
                    rx.utils.imports.ImportVar(
                        tag="useUser"
                    ),
                },
            },
        )

    def _get_hooks(self) -> str | None:
        return """
        const { isSignedIn, user, isLoaded } = useUser();
        console.log({ isSignedIn, fullName: user?.fullName, isLoaded }); // Log the values to the console
        return { name: user?.fullName, user_signed_in: isSignedIn };
        """

    def get_event_triggers(self):
        return {
            **super().get_event_triggers(),
            "on_mount": lambda: [
                rx.call_script(
                    self._get_hooks(),
                    callback=ClerkUserState.update_user_info
                )
            ],
        }

    @staticmethod
    def _get_app_wrap_components() -> dict[tuple[int, str], rx.Component]:
        return {
            (1, "ClerkProvider"): ClerkProvider.create(
                publishable_key=os.environ.get("CLERK_PUBLISHABLE_KEY"),
                after_sign_in_url="/",
                after_sign_up_url="/",
                after_sign_out_url="/"
            ),
        }

    def render(self):
        return rx.text("render")
