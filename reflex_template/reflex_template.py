"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import reflex_clerk as clerk

import os
import logging
from .components.navbar import navbar

logger = logging.getLogger(__name__)


class State(rx.State):
    """The app state."""

    def handle_get_code(self) -> rx.Component:
        logger.info("a user gets the code!")

        return rx.redirect(
            "https://github.com/dentro-innovation/reflex_template", external=True
        )


def AppContent() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading("Reflex Template", padding="1em"),
                rx.box(
                    rx.cond(
                        clerk.ClerkState.user.first_name,
                        rx.text(f"How are you {clerk.ClerkState.user.first_name}?"),
                    ),
                    rx.text(
                        f"I know your email from Clerk: {clerk.ClerkState.user.email_addresses[0].email_address}"
                    ),
                    rx.text(f"Are you logged in: {clerk.ClerkState.is_signed_in}"),
                    padding="1em",
                ),
                rx.divider(),
                rx.vstack(
                    rx.text(
                        "Reflex template made by the guys from ",
                        rx.link("dentroai.com", href="https://dentroai.com"),
                        " with:",
                    ),
                    rx.text("- Clerk Integration for user management"),
                    rx.text("- Betterstack Integration to visualize logs"),
                    rx.text("- Docker compose files for production"),
                    rx.text("- Github Action for automatic deployment"),
                    rx.text(),
                    rx.button("Get the code", on_click=State.handle_get_code),
                    padding="3em",
                ),
                align="center",
            )
        ),
    )


def index() -> rx.Component:
    return clerk.clerk_provider(
        rx.center(
            clerk.signed_in(AppContent()),
            clerk.signed_out(
                rx.center(
                    clerk.sign_in(),
                    padding_top="10em",
                )
            ),
        ),
        publishable_key=os.getenv("CLERK_PUBLISHABLE_KEY"),
        secret_key=os.getenv("CLERK_SECRET_KEY"),
    )


app = rx.App()
app.add_page(index)
