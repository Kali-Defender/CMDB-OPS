import paramiko

def upload_file(host, port, username, password, file_data, remote_path):
       client = paramiko.SSHClient()
       client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       try:
           client.connect(host, port=port, username=username, password=password, timeout=5)
           sftp = client.open_sftp()                    # 开文件通道
           with sftp.file(remote_path, 'wb') as f:      # 打开远程文件（写二进制）
               f.write(file_data)                       # file_data 是 bytes（文件内容）
           sftp.close()
           return {"success": True, "output": f"已上传到 {remote_path}"}
       except Exception as e:
           return {"success": False, "output": str(e)}
       finally:
           client.close()