apt update && apt install -y python python-pip
pip install gradescope-utils>=0.3.1 boto3 google-cloud-storage azure-storage-blob

cd /autograder/source
git clone https://github.com/chiache/csce410_f22_proj4_tests -b autograder
