<?php

function openWin() {
    myWindow = window.open("", "", "width=100, height=100");  // Opens a new window
}

function resizeWin() {
    myWindow.resizeTo(250, 250);                             // Resizes the new window
    myWindow.focus();                                        // Sets focus to the new window
}

?>