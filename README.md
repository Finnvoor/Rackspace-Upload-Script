# Rackspace-Upload-Script
A python/automator script to upload an image to [KrakenIO](https://kraken.io) for compression and host it on [Rackspace](https://www.rackspace.com).

### Usage

Intall the required modules:

    pip install krakenio
    pip install send2trash
 
Open Upload.workflow and replace the following lines:
    
    KRAKEN_CLIENT_ID     # Your Kraken API id
    KRAKEN_CLIENT_SECRET # Your Kraken API secret
    RACKSPACE_USERNAME   # Your Rackspace username
    RACKSPACE_KEY        # Your Rackspace key

Move the automator action 'Upload.workflow' to Library/Services and right click any image, select 'Upload', and it will be uploaded to kraken to be compressed and hosted on your rackspace account.
