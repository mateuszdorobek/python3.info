// Uruchamianie: https://script.google.com/
// Dokumentacja: https://developers.google.com/apps-script/reference/gmail/

function main() {
  const SPREADSHEET = 'https://docs.google.com/spreadsheets/d/.../edit#gid=0'
  const SHEET = 'stats'
  const LABEL = 'moja etykietka'

  let output = SpreadsheetApp.openByUrl(SPREADSHEET).getSheetByName(SHEET);
  let label = GmailApp.getUserLabelByName(LABEL);

  var pageStart = 0;
  var pageSize = 50;
  var page;

  do {
    page = label.getThreads(pageStart, pageSize)

    page.forEach(thread => {
        var messages = thread.getMessages();

        // Message API:  https://developers.google.com/apps-script/reference/gmail/gmail-message
        messages.forEach(function(message) {
          output.appendRow([
              message.getId(),
              message.getDate(),
              message.getFrom(),
              message.getTo(),
              message.getCc(),
              message.getBcc(),
          ]);
        });
    });

    pageStart += pageSize;
    Utilities.sleep(1000);

  } while(page.length > 0)
}
