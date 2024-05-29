import reflex as rx
import reflex_clerk as clerk


def navbar():
    return rx.hstack(
        rx.image(
            src="/dentro_logo.svg",
            fallback="FA",
            variant="solid",
            width="8em",
            height="auto",
        ),
        rx.spacer(),
        clerk.user_button(),
        width="100vw",
        padding="1em",
        position="sticky",
        top="0",
        z_index="100",
    )
