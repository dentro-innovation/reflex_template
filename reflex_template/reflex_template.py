"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
import reflex as rx
from .utils.clerk_wrapper import signed_in, signed_out, sign_in, user_button, ClerkUser, ClerkUserState
import logging
from .components.navbar import navbar

logger = logging.getLogger(__name__)

class State(rx.State):
    """The app state."""
    
def AppContent() -> rx.Component:
    
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading("Hello there!"),
                rx.cond(
                    ClerkUserState.name,
                    rx.text(f"How are you {ClerkUserState.name}?"),
                ),
                rx.text(f"Your email is: {ClerkUserState.email}"),
            )
        )
    )

def index() -> rx.Component:
    return rx.center(
        ClerkUser.create(),
            signed_in(
                AppContent()
            ),
            signed_out(
                rx.center(
                    sign_in(),
                    padding_top="10em",
                )
            ),
        )


app = rx.App()
app.add_page(index)
