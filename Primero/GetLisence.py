###############################################
# TX SX spoof ID unpacker - by Reacher17 #
# Thanks to the following: 
# Inaki - license.dat
# Zoria - Linkynimes
# Shadow, Darkstorm, B&ender, Heykyz
###############################################
from Crypto.Cipher import AES
from Crypto.Util import Counter
import os
import hashlib
from binascii import hexlify as _hexlify, unhexlify
import subprocess
import sys
import pip

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

#print(installed_packages)

[
    "pycryptodome",
    "pycryptodomex",
]

def install():
    try:
        if not 'pycryptodome' in installed_packages:
            pip.main(['install', "pycryptodome"])
        if not 'pycryptodomex' in installed_packages:
            pip.main(['install', "pycryptodomex"])        
    
    except ImportError:
        print("Can't install pycryptodome or pycryptodomex")

install()

def hexlify(b: (bytes, bytearray)) -> str:
    return _hexlify(b).decode("utf8")

def aes_ctr_dec(buf, key, iv):
    hex_val = (iv.hex())
    ctr = Counter.new(128, initial_value=int(hex_val, 16))
    return AES.new(key, AES.MODE_CTR, counter=ctr).encrypt(buf)

# SXOS fingerprint - use switch fingerprint that goes with the donated licence

#spare license
#sxos_fingerprint = ("25E2DCB7D00032334732333000011100")
#goodlic = ("92F2DDC544194444C15F4A3FD6A05D1E3C3C0D518CDB9BB0C0C865C72C1909B9E0471B5AAE1A0D3F803176AA26D5AB3A4F30D9377D0BC54962BBDF93B7E34B555D53D21D2538B2DFC006909593AC032F6F6FB42C8C8CB3ACA81810B6994BAE452DE9AE7412DB6A17717E5E22B79A5DBE05FCD00872A3029F84E280C8F1FDAC8BDFB37F5B047493BFE72C06027FCE914CAE3A225E75B024DD795A1651CC4DA91324364B1A90522B219B7F9101145EDA0D31EE7AEF687E1D85CAB85B04A317134EA5CD073CD0BE554ED8E512450FCE6DFDFDBCD523F2A85AF10D1F3A66391B2B281741879EFA26B1114B1042BF4AB2E3D2A3BB36B53CEEDBFE2B6FA90F838062C0")

sxos_fingerprint = ("5602D40FA505523444544A4200011500")
goodlic = ("B2ECDB5F517EDB111D906C8D153AEFFCE6D17282E9955116600EBBAE4770FA21A33A78CB5FCB7A9431D6D9CE20B02879E84D899310F2F59ABD716143A5381A53D55944E37EECFE166AEA6FA334469CDDF868F99509C6D95CCFC0B9DB63F8377DD6E833E8989F7C20FFED34F4F0AF054D60C28455E6933C5158F4F72E8C44C9F695E5EFAD756FF3A8D3CCF1633AC72AFB5E53CFE3ECBE25E31FA49FD6397D75E5DF38EC61DC897E02D1A44613B8A4359FB0292D95173BDF96B5AE5D8EEF821B1CFB6AEFA759E0A51EBD083C3CD751B5E2EA20201EAC2A19AE37712036DF4E7A05A1DE757FA5F5B440BA303A477063D9D2957EE71FA370217532684BA1E55C097D")

fingerprint = unhexlify(sxos_fingerprint)

payload81_key = unhexlify("12280A64B7A487E99864CD2E22393C87")
payload81_ctr = unhexlify("C28124EAA147BEE8EF865E2AE8496834")
s2_key = unhexlify("47E6BFB05965ABCD00E2EE4DDF540261")
s2_ctr = unhexlify("8E4C7889CBAE4A3D64797DDA84BDB086")
s3_key = unhexlify("D548D48DBA299604CED1AE5B47D8429C")
s3_ctr = unhexlify("428DB51A85E4940D37648FEC66BA2C78")
fw_key = unhexlify("81F555CC58EF03CB41BD81C90A8E8F79")
fw_ctr = unhexlify("A4C122884E6C8979E3E3E0F07D116E52")
license = ("46726565204C6963656E636500")

patch_d = unhexlify("3B980014")
patch_spoof = unhexlify("0000014A8D2981520D40B072AE0D40390F008052DF010F6B01F8EC54010000140A208CD28A23B0F24B3140A90D2881D20D40B0F2AB3100A9B867FF17")
patch_license1 = unhexlify("000080D2C0035FD6")
patch_license2 = unhexlify("C0CC80D2C0035FD6")
patch_s2 = unhexlify("00008052C0035FD6")


header = 'header.bin'
boot = 'boot.dat'
bootbin = 'boot.bin'
stage2 = 'stage2_40008100.bin'
stage3 = 'stage3_40020000.bin'
payload81 = 'payload_81000000.bin'
rommenu = 'rommenu.bin'

f = open(boot, "rb")
bootin = f.read()

bootout = open(bootbin, "wb")
bootout.write(bootin)


#payload80000000.bin
pay81 = open(payload81, "wb")
pay81.write(aes_ctr_dec(bootin[0x201E0:0x1F6DE0], payload81_key, payload81_ctr))
pay81.seek(0x19FF14)
pay81.write(patch_d)
pay81.seek(0x1C6000)
pay81.write(patch_spoof)
pay81.seek(0x1C6100)
pay81.write(fingerprint)
pay81.seek(0x0)

with open(payload81, 'rb') as f:
    bytes = f.read()
    sha256_pay81 = hashlib.sha256(bytes).hexdigest()  
print(sha256_pay81)

bootout.seek(0x201E0)
bootout.write(aes_ctr_dec(bytes, payload81_key, payload81_ctr))
#------------------

#stage3 40020000.bin
stage3_in = open(stage3, "wb")
stage3_in.write(aes_ctr_dec(bootin[0x11500:0x1BB70], s3_key, s3_ctr))
stage3_in.seek(0xA620)
stage3_in.write(unhexlify(sha256_pay81))
stage3_in.seek(0x0)

with open(stage3, 'rb') as f:
    bytes = f.read()
    sha256_stage3 = hashlib.sha256(bytes).hexdigest()
print(sha256_stage3)

bootout.seek(0x11500)
bootout.write(aes_ctr_dec(bytes, s3_key, s3_ctr))
#------------------

#stage2 40008100.bin
stage2_in = open(stage2, "wb")
stage2_in.write(aes_ctr_dec(bootin[0x100:0x110D0], s2_key, s2_ctr))
stage2_in.seek(0x45C0)
stage2_in.write(patch_s2)
stage2_in.seek(0x0)

with open(stage2, 'rb') as f:
    bytes = f.read()
    sha256_stage2 = hashlib.sha256(bytes).hexdigest()
print(sha256_stage2)

bootout.seek(0x100)
bootout.write(aes_ctr_dec(bytes, s2_key, s2_ctr))
#-------------------
#header.bin
header_m = open(header, "wb")
header_m.write(bootin[0x0:0xE0])
header_m.seek(0x10)
header_m.write(unhexlify(sha256_stage2))
header_m.seek(0x0)

with open(header, 'rb') as f:
    bytes = f.read()
    sha256_header = hashlib.sha256(bytes).hexdigest()
print(sha256_header)
bootout.seek(0x0)
bootout.write(bytes)
bootout.seek(0xE0)
bootout.write(unhexlify(sha256_header))

#------------------

#ROMMENU.bin
rom_in = open(rommenu, "wb")
rom_in.write(aes_ctr_dec(bootin[0x11EBA40:0x15c8080], fw_key, fw_ctr))
rom_in.seek(0x7CA0)
rom_in.write(patch_license1)
rom_in.seek(0x7D40)
rom_in.write(patch_license1)
rom_in.seek(0x14AE0)
rom_in.write(patch_license2)
rom_in.seek(0x13AAD0)
rom_in.write(unhexlify(license))
rom_in.seek(0x0)

with open(rommenu, 'rb') as f:
    bytes = f.read()
    sha256_rommenu = hashlib.sha256(bytes[0x610:0x1AD610]).hexdigest()
print(sha256_rommenu)

rom_in.seek(0x18)
rom_in.write(unhexlify(sha256_rommenu))
rom_in.seek(0x0)
rom_in = open(rommenu, "rb")
rom_in2 = rom_in.read()
bootout.seek(0x11EBA40)
bootout.write(aes_ctr_dec(rom_in2, fw_key, fw_ctr))
#------------------
#------------------

f = open(bootbin, "rb")
bootin = f.read()
bootout = open(boot, "wb")
bootout.write(bootin)

validlic = open("license.dat", "wb")
validlic.write(unhexlify(goodlic))
validlic.close()


f.close()
pay81.close()
stage2_in.close()
stage3_in.close()
header_m.close()
bootout.close()
rom_in.close()

os.remove("boot.bin")
os.remove("header.bin")
os.remove("payload_81000000.bin")
os.remove("stage2_40008100.bin")
os.remove("stage3_40020000.bin")
os.remove("rommenu.bin")

print("Done!")
