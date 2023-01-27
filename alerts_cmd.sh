#(notifies)

terminal-notifier -message "Hello, this is my message" -title "Message Title"

osascript -e 'display notification "Notification text" with title "Notification Title" subtitle "Notification sub-title" sound name "Pop"'
echo Successful
