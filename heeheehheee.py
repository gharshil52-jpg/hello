from abc import ABC, abstractmethod

import streamlit as st


class Button(ABC):
    """Abstract interface for button-like controls."""

    @property
    @abstractmethod
    def label(self) -> str:
        """Return the visible button text."""

    @abstractmethod
    def render(self) -> bool:
        """Display the control and return whether it was clicked."""

    @abstractmethod
    def on_click(self) -> None:
        """Run the action associated with a button press."""


class StreamlitButton(Button):
    def __init__(self, label: str, key: str | None = None, disabled: bool = False):
        self._label = label
        self._key = key
        self._disabled = disabled

    @property
    def label(self) -> str:
        return self._label

    def render(self) -> bool:
        clicked = st.button(self._label, key=self._key, disabled=self._disabled)
        if clicked:
            self.on_click()
        return clicked

    def on_click(self) -> None:
        st.session_state["last_clicked_button"] = self._label


# Example usage.
st.title("Hello, World!")
st.header("This is a simple Streamlit app.")

button = StreamlitButton("Click me!", key="hello_button")
if button.render():
    st.success(f"You clicked the button ")
