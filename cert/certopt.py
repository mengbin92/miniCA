from cryptography import x509
from cryptography.x509 import NameOID
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization,hashes
from cryptography.hazmat.primitives.asymmetric import ec,rsa
import datetime

def generatekey(keytype,bits):
    if keytype == 'rsa':
        return rsa.generate_private_key(65537,bits,default_backend())
    elif keytype == 'ec':
        return ec.generate_private_key(ec.SECP521R1(),default_backend())

def createCSR(key,common,country,locality,province,organization,organizationunit,email):
    csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME,common),
        x509.NameAttribute(NameOID.COUNTRY_NAME,country),
        x509.NameAttribute(NameOID.LOCALITY_NAME,locality),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME,province),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME,organization),
        x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME,organizationunit),
        x509.NameAttribute(NameOID.EMAIL_ADDRESS,email),
    ])).add_extension(
        x509.BasicConstraints(ca=False, path_length=None), critical=False,
    ).sign(key,hashes.SHA256(),default_backend())
    return csr

def selfsigncert(key,csr,days):
    cacert = x509.CertificateBuilder().issuer_name(
        csr.subject
    ).subject_name(
        csr.subject
    ).public_key(
        csr.public_key()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=days)
    ).serial_number(
        0x1
    ).add_extension(
        x509.BasicConstraints(ca=True,path_length=None),
        critical = True
    ).add_extension(
        x509.KeyUsage(digital_signature=False, content_commitment=False, key_encipherment=False, data_encipherment=False, key_agreement=False, key_cert_sign=True, crl_sign=True, encipher_only=None, decipher_only=None),
        critical = False
    ).add_extension(
        x509.SubjectKeyIdentifier.from_public_key(key.public_key()),
        critical = False
    ).add_extension(
        x509.AuthorityKeyIdentifier.from_issuer_public_key(key.public_key()),
        critical = False
    ).add_extension(
        x509.SubjectAlternativeName([
            x509.RFC822Name(csr.subject.get_attributes_for_oid(NameOID.EMAIL_ADDRESS)[0].value),
        ]),
        critical = False
    ).add_extension(
        x509.IssuerAlternativeName([
            x509.RFC822Name(csr.subject.get_attributes_for_oid(NameOID.EMAIL_ADDRESS)[0].value),
        ]),
        critical = False
    ).sign(key,hashes.SHA256(),default_backend())
    return cacert

def signuser(key,rootca,csr,days):
    user_cert = x509.CertificateBuilder().subject_name(
        csr.subject
    ).issuer_name(
        rootca.subject
    ).public_key(
        csr.public_key()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=days)
    ).serial_number(
        x509.random_serial_number()
    ).add_extension(
        x509.BasicConstraints(ca=False,path_length=None),
        critical = False
    ).add_extension(
        x509.KeyUsage(digital_signature=True, content_commitment=True, key_encipherment=True, data_encipherment=False, key_agreement=False, key_cert_sign=False, crl_sign=False, encipher_only=None, decipher_only=None),
        critical = False
    ).sign(key,hashes.SHA256(),default_backend())
    return user_cert

if __name__ == '__main__':
    key = generatekey('ec',123)
    csr = createCSR(key,'rootca','CN','beijign','beijing','miniCA','test','123@qq.com')
    cacert = selfsigncert(key,csr,7300)
    exts = cacert.extensions
    for ext in exts:
        print(ext)