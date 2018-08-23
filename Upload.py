from krakenio import Client        # KrakenIO API module
from send2trash import send2trash  # Move file to trash module
from datetime import datetime
import subprocess, sys, os


# Kraken API Settings ------------------------------------------------------------------------
api = Client('KRAKEN_CLIENT_ID', 'KRAKEN_CLIENT_SECRET')
data = {
    'wait': True,
    'cf_store': {
        'user': 'RACKSPACE_USERNAME',
        'key': 'RACKSPACE_KEY',
        'container': 'Kraken',
        'ssl': True
    }
}

# Copy text to clipboard ---------------------------------------------------------------------
def writeToClipboard(output):
	process = subprocess.Popen(
		'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
	process.communicate(output.encode('utf-8'))

# Display system notification ----------------------------------------------------------------
def showNotification(title, text, subtitle):
    os.system("""
              osascript -e 'display notification "{}" with title "{}" subtitle "{}"'
              """.format(text, title, subtitle))

# Main Program -------------------------------------------------------------------------------
def main():
    time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S.png")

    for f in sys.argv[1:]:
    	os.rename(f, time)
    	size = os.path.getsize(time) / 1000

    result = api.upload(time, data);

    if result.get('success'):
    	send2trash(time)
    	writeToClipboard(result.get('kraked_url'))
    	newsize = result.get('kraked_size')/1000
    	showNotification('Upload to Rackspace', ('Savings: ' + str(size-newsize) + 'kb'), 'Image URL copied to clipboard')
    else:
    	writeToClipboard(result.get('message'))
    	showNotification('Upload to Rackspace', result.get('message'), 'Error')

# --------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
