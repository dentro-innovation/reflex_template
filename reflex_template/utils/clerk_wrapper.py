import reflex as rx
import os

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


clerk_provider = ClerkProvider.create
signed_in = SignedIn.create
signed_out = SignedOut.create
sign_in = SignIn.create
user_button = UserButton.create

sign_in_button = SignInButton.create
sign_up_button = SignUpButton.create
sign_out_button = SignOutButton.create


class ClerkUserState(rx.State):
    email: str = ""
    name: str = ""
    
    def set_email(self, email: str):
        self.email = email
        
    def set_name(self, name: str):
        self.name = name

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
                "react": {
                    rx.utils.imports.ImportVar(
                        tag="useEffect"
                    ),
                    rx.utils.imports.ImportVar(
                        tag="useContext"
                    ),
                },
                "/utils/context": {
                    rx.utils.imports.ImportVar(
                        tag="EventLoopContext"
                    ),
                },
                "/utils/state": {
                    rx.utils.imports.ImportVar(
                        tag="Event"
                    ),
                },
            },
        )

    def _get_hooks(self) -> str | None:
        return """
        const { isSignedIn, user, isLoaded } = useUser();
        const [addEvents] = useContext(EventLoopContext);

        useEffect(() => {
        if (isLoaded && user) {
            const emailAddress = user?.primaryEmailAddress?.emailAddress;
            const name = user?.fullName;
            if (emailAddress) {
            addEvents([Event("state.clerk_user_state.set_email", {"email": emailAddress})], {}, {}); // Add the event to set the email
            }
            if (name) {
            addEvents([Event("state.clerk_user_state.set_name", {"name": name})], {}, {}); // Add the event to set the name
            }
        }
        }, [isLoaded, user, addEvents]);
        
        //console.log({ isSignedIn, emailAddress: user?.primaryEmailAddress.emailAddress, isLoaded }); // Log the values to the console
        """

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
