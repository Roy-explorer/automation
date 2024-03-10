# **Setup**  
Set virtual environment, and use pip to install libraries in command prompt.
## 1.Table Extraction  
### 1. **Extract csv files and tables from html**  
    ```python
    pip install pandas  #(Install in jupyter: !pip install pandas)
    # The library for table extraction from html
    pip install lxml  
    ``` 
    If use jupyter in vscode, install the commended libraries for jupyter

### 2. **Extract Tables from PDFs**  
   Use "camelot" library to extract the table,but we have to install necessary libraries.
   ```  
   pip install tk  
   pip install ghostscript
   ```  

   - #### **Error:**  
        However, there is usually an error about **"missing ghostscript DLL"** while using vscode on Windows.  

        To fix this problem, we need to download the license on the website according to your own platform.  
        **Website :** https://camelot-py.readthedocs.io/en/master/user/install-deps.html  

        reference: https://blog.csdn.net/Sarah_608/article/details/132762960  

        1. **Click "downloaad pages"**  
        <img src= "../Markdown Picture/1.Table Extraction/image-4.png" width=700>  
        <img src= "../Markdown Picture/1.Table Extraction/image.png" width=700>

        2. Run the executable file downloaded, and install the "GPL Ghostscript" in ``` Lib\site-packages ``` in the virtual environment.  
        <img src= "../Markdown Picture/1.Table Extraction/image-2.png" width=700>  
        <img src= "../Markdown Picture/1.Table Extraction/image-3.png" width=700>  
        3. Check DLL file (eg. Windows 64bit : File gsdll64.dll below)  
        <img src= "../Markdown Picture/1.Table Extraction/image-1.png" width=700>  

        4. **Result (Command line):**  
        <img src= "../Markdown Picture/1.Table Extraction/image-5.png" width=700>  


   
