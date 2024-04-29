"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
import reflex as rx
from .utils.clerk_wrapper import use_user, clerk_provider, signed_in, signed_out, sign_in, user_button, ClerkUser, ClerkUserState


class State(rx.State):
    """The app state."""
    
# def AppContent() -> rx.Component:
#     user_info = use_user()
#     user = rx.call_script("useUser()")
#     # is_signed_in = user_info['isSignedIn']
#     # user = user_info['user']
#     # is_loaded = user_info['isLoaded']
    
#     return rx.vstack(
#         rx.hstack(
#             rx.text(f"Hello my dear {user}!"),
#             user_button(),
#         )
#     )

def index() -> rx.Component:
    return rx.center(
        clerk_provider(
        rx.text("Hello World!"),
            ClerkUser.create(
                user_button(),
            ),
            rx.button("Print User Info", on_click=ClerkUserState.print_user_info)
        )
    )


# def index() -> rx.Component:
#     return rx.center(
#         clerk_provider(
#             signed_in(
#                 AppContent()
#             ),
#             signed_out(
#                 rx.center(
#                     sign_in(),
#                     padding_top="10em",
#                 )
#             ),
#         ),
#     )


app = rx.App()
app.add_page(index)
