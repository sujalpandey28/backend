import os
def initialise_env():
    os.environ['DB_HOST'] = 'localhost'
    os.environ['DB_PASSWORD'] = '1234'
    os.environ['DB_USER'] = 'postgres'
    os.environ['DB_DATABASE'] = 'test_db'
    os.environ['DB_PORT'] = '5432'
    
    # os.environ['FIREBASE_TYPE'] = 'service_account'
    # os.environ['FIREBASE_PROJECT_ID'] = 'assistbloom-1b2c5'
    # os.environ['FIREBASE_PRIVATE_KEY_ID'] = '9f1d4c070e1232fff4876f51e42e13a58008d407'
    # os.environ['FIREBASE_PRIVATE_KEY'] = '-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDKETPyBBycb7S2\nbRZJj7KkXv71HWX6mj2+H9N+pUkMqziY4615TfIIQ0nkhAve6v1c6uQRF7I1xadB\nnpAHpgWi583ThYEfD6wi00cFQMRvgEfVenev7dCzlEwSaGEef908BB2nOub9w4f+\nwiI821iKRPmIcrewEwXzvSUMB2ledjpIxgjlFGqCwMFwnxNMX3Qjlcvx/pJSRgHF\nOQIQjFOE6VcbXK6/OHDml2oapBPqxAiOpSTtqKzlkgg8+QcS8JbIEOCO5Z5R8lIE\n71dD/NQ0utVWqnS2qqN2bqhA+JX+2gHuFCVm9bhEF1ZkdgdwMXFKf+rHobTtk96r\nkf4oyBtzAgMBAAECggEACx8NQ9m0FWwUfyHb4yqUg3VzBNycW0GX+lnYExVXwum9\nkLSfPJjspEXH0FrwKFG4ph+Lc+Fg/pKlVPg8Jx+dGc02R9kGNUZwi+4i74gUB6sA\nySAXbEhjfy6/TRgPmFUjQQVc+HJGelsDpiLbLYxJADsxnK/rqjYx0qtrWZEi3H7+\nJxML/UNRktQLaSdtf2hsAFTkKObcp2eL11x26WwwidZFCAyUtwDe9hLW5kqnY3PW\nTGxcfKKkxcbl8+TzmHFN6SRz59kfy2k9i/ajebmW/E7t1YRhmBoyQawoFvZ3TQDh\nDyGyON07f14JuDyNxTA16NzhlZfRYxEHJvD1WUe0sQKBgQD7T5KJLXlvYq+8usT2\nNOcZp5QVJxo7e5umziwVDz2QKKkjas50gSeMkCYUyd54+EP63ighJ9W0d+RRdbTp\n6Sd0iGv4FPT7Q8+U2iUifyrxfCF08yT1OQ2FnvaSEtRmhSHsoR/AAG0ojFL8W/Bt\nBjVEcORFk4GmYDjqCoebpLZfmwKBgQDN1mkCEqRca0EM27Ev1xptT00fom+Mi9h4\nbOpFhD7wWvylFQKRtfgNyjbISFuYGc2lDnsa1tkv5kkFtxdLjTnijdSrawiUiekK\ncUDFYt9R8XRjsV0bPgllZFJGXM1d28qIImNfeFDAOIuRKO/roCOO7f37eSdMKj9U\n3uvYhvmtCQKBgHecL8pKcnmpJqtU2Vm1ZCi5sak/qySUeEiz6Bc94bczIw1QUGLy\n9bfZA8bxLYm13+UOx1rAct4qEekTdL+/0J+OLpUspEzSwYG/Md1xWScGRYY8E2MD\nfIQUXJa5j44b30GYjlv71/hskTK7L3s0cTXZ5UuYISTmty/tQw25H3PxAoGAAVAW\nx16bEcPVXGGiVa3Hi17wHP2KPJk/vjTjoaHgTOQnrF3f8FH6zQu3Ibvkaanwd9cJ\nzfgE1ptfZ9vtGBxEfD9vVdCO83OVuu1R/nBNAFbL6T7eWyggIzdqluxMmwal2gxu\nGdPIoBE8QqbCMPyKfYTjE9GIAKJcWQw68NybhxECgYBS6P34I2KC9IzgM06gdY1z\nZpPTWNIVI818khA6Ai5FkVs/tCDmKDXuwjok1gY71PWQf8F2oMifmHDnRC30e7c0\nNsw7b/+PTBSOk80WVS5muIbM1Nm9fEvtLV2Tux6yR58f5Dvs461058yiHx3s4wQi\nmipmUPUbVdK/nYLpmrqrrA==\n-----END PRIVATE KEY-----\n'
    # os.environ['FIREBASE_CLIENT_EMAIL'] = 'firebase-adminsdk-1we38@assistbloom-1b2c5.iam.gserviceaccount.com'
    # os.environ['FIREBASE_CLIENT_ID'] = '103100153917197892959'
    # os.environ['FIREBASE_AUTH_URI'] = 'https://accounts.google.com/o/oauth2/auth'
    # os.environ['FIREBASE_TOKEN_URI'] = 'https://oauth2.googleapis.com/token'
    # os.environ['FIREBASE_AUTH_PROVIDER_X509_CERT_URL'] = 'https://www.googleapis.com/oauth2/v1/certs'
    # os.environ['FIREBASE_CLIENT_X509_CERT_URL'] = 'https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-1we38%40assistbloom-1b2c5.iam.gserviceaccount.com'
    # os.environ['FIREBASE_UNIVERSE_DOMAIN'] = 'googleapis.com'
    # os.environ['SECRET_KEY'] = 'c11e2825b249089e2f763dc34ab96871b5809f10479336152fc1eb74a1a75690'
    # os.environ['SPACES_END_POINT'] = 'https://assistbloom-attachments.blr1.digitaloceanspaces.com'
    # os.environ['SPACES_REGION'] = 'blr1'
    # os.environ['SPACES_ACCESS_KEY_ID'] = 'DO00BJEBD7HJANNMLHX6'
    # os.environ['SPACES_SECRET_KEY'] = 'hQKwyGHfRBSu1sUIMvEn1jlHQ4cZSMbkKpd9Rf9Zxgk'

    # os.environ['DB_HOST'] = 'assistbloom-production-do-user-15840154-0.c.db.ondigitalocean.com'
    # os.environ['DB_PASSWORD'] = 'AVNS_32DaX_LsD3t3Dmy2d8w'
    # os.environ['DB_USER'] = 'doadmin'
    # os.environ['DB_DATABASE'] = 'production_db'
    # os.environ['DB_PORT'] = '25060'

    print("Initialised Env variables...")