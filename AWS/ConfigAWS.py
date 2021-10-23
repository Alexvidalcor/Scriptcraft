import subprocess
from pathlib import Path
import getpass as gp
import boto3
from botocore.exceptions import ClientError

def ValidCredentials():
    try:
        sts = boto3.client('sts')
        sts.get_caller_identity()
        return "Valid"
    except ClientError:
        print("Credenciales no válidas")
        return "Invalid"

def CheckDirectories():
    mainUser = gp.getuser()
    if Path(f"/home/{mainUser}/.aws").exists():
        print("Carpeta AWS detectada")    
    else:
        print("¿Primera vez en AWS? Creando directorios...")
        Path(f"/home/{mainUser}/.aws").mkdir(parents=True, exist_ok=True)
        print("OK")

def CreateCredentials(accessID, keyID, tokenID):
    try:
        f = open(f"/home/{gp.getuser()}/.aws/credentials", "x+")
        print("Escribiendo credenciales...")
        f.write("[default]\n")
        f.write(f"aws_access_key_id={accessID}\n")
        f.write(f"aws_secret_access_key={keyID}\n")
        if tokenID != "":
            f.write(f"aws_session_token={tokenID}\n")
        f.close
        print("OK")
    except FileExistsError:
        print("Modificando viejas credenciales...")
        Path(f"/home/{gp.getuser()}/.aws/credentials").unlink()
        CreateCredentials(accessID, keyID, tokenID)

def AskCredentials():
    accessPass = gp.getpass("Introduce access: ")
    keyPass = gp.getpass("Introduce key: ")
    tokenPass = gp.getpass("Introduce tu token (opcional):")
    return accessPass, keyPass, tokenPass

if __name__ == "__main__":
    createdCheck = CheckDirectories()
    accessPass, keyPass, tokenPass = AskCredentials()
    if keyPass != "" and accessPass != "":
        CreateCredentials(accessPass, keyPass, tokenPass)
    else:
        print("Credenciales vacías o incompletas. Programa terminado")
