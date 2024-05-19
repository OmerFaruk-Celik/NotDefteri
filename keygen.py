import subprocess
import os

def generate_ssh_key(key_filename="id_rsa"):
  """SSH anahtar çiftini oluşturur ve kamu anahtarını bir dosyaya kaydeder.
  
  Args:
    key_filename: Özel anahtarın dosya adı. Kamu anahtarı otomatik olarak aynı isimle ".pub" uzantılı olarak oluşturulur.
  """
  try:
    bilgiler_dosyasi = os.path.join(os.path.expanduser("~"), "github","Python_OTO_COMMIT", "bilgiler.txt")
    with open(bilgiler_dosyasi, "r") as f:
      username, email, tokenn = f.readline().strip().split(",")
      
    print(email)
    os.system("rm -rf ~/.ssh/id_rsa* ")
    os.system(f"ssh-keygen -t rsa -b 4096 -C '{email}' -f ~/.ssh/id_rsa -N ''")
    print(f"SSH anahtar çifti oluşturuldu. Kamu anahtar {key_filename} dosyasına kaydedildi.")
  except FileNotFoundError:
    print("bilgiler.txt dosyası bulunamadı. Lütfen dosyanın var olduğundan emin olun.")
  except IndexError:
    print("bilgiler.txt dosyasında e-posta adresi bulunamadı. Lütfen dosyayı kontrol edin.")
  except Exception as e:
    print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
  # varsayılan dosya adı kullanarak anahtarı oluştur
  generate_ssh_key() 

  # .ssh dizini yoksa oluştur
  ssh_dir = os.path.expanduser("~/.ssh")
  if not os.path.exists(ssh_dir):
      os.makedirs(ssh_dir)


