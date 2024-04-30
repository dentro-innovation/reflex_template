"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
import reflex as rx
from .utils.clerk_wrapper import signed_in, signed_out, sign_in, user_button, ClerkUser, ClerkUserState
import logging
from .components.navbar import navbar

logger = logging.getLogger(__name__)

class State(rx.State):
    """The app state."""
    
    def handle_get_code(self) -> rx.Component:
        logger.info(f"user {ClerkUserState.email} gets the code!")
        
        return rx.redirect(
            "https://github.com/dentro-innovation/reflex_template",
            external=True
        )
    
        
    
def AppContent() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading("Reflex Template", padding="1em"),
                rx.box(
                    rx.cond(
                        ClerkUserState.name,
                        rx.text(f"How are you {ClerkUserState.name}?"),
                    ),
                    rx.text(f"I know your email from Clerk: {ClerkUserState.email}"),
                    padding="1em",
                ),
                rx.divider(),
                rx.vstack(
                    rx.text("Reflex template made by the guys from ", rx.link("dentroai.com", href="https://dentroai.com"), " with:"),
                    rx.text("- Clerk Integration for user management"),
                    rx.text("- Betterstack Integration to visualize logs"),
                    rx.text("- Docker compose files for production"),
                    rx.text("- Github Action for automatic deployment"),
                    rx.text(),
                    rx.button("Get the code", on_click=State.handle_get_code),
                    padding="3em",
                ),
                align="center"
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
