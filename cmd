osascript <<EOT
    activate
    text returned of (display dialog "%s" default answer "" buttons {%b, %b} default button 1 with title "Type A Value")
EOT
