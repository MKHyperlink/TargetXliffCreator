Create target localization xliff file for Xcode import.

####Introduce
This tool is what you want.
If you are using storyboard to develop your iOS app UI and want to localize your app by single localization file. 

As we know, the localization files are created by storyboard separately and we need maintain multiple localization files.
The other shortcomings is when you add/remove UI component in storyboard, it needs create localization file again. And your storyboard localization files will be initialized, all you done before will gone.

This tool can use single localization file to modify others localization files that created by storyboard.
Just few steps:
1. Export Xliff localization file. ((The Xliff file is Apple recommend localization file format)
2. Using this tool localize Xliff file.
3. Import Xliff localization file.
4. All your storyboard localization files will localized.


####Dependent module

1. lxml  
If you have problem with install lxml module in Mac OS. Please trying run the commandline below:  
(Maybe needs sudo) `STATIC_DEPS=true pip install lxml`

####Guideline
1. Input a Key instead of a text . ex. Key "firstPg_str01" as screenshot below  
![ScreenShot](/docs/screenshot/storyboard1.png)
2. Export xliff file from your project.  
![ScreenShot](/docs/screenshot/localizationExport.png)
3. Select "Development Language Only". It will export a Base Xliff file for translation.  
![ScreenShot](/docs/screenshot/baseLangExport.png)
4. Execute $python targetXliff.py [base_file] [source_file] [target_language]  
    ex. `$python targetXliff.py en.xliff infoPlist.plist ja`      
![ScreenShot](/docs/screenshot/localizationFile.png)  
5. After step 4. The target xliff file with target language will be created.   
    It's according to mapping the text value of note tag in en.xliff with Key in infoPlist.plist file.
6. The final step is import created Target xliff file by Xcode.
![ScreenShot](/docs/screenshot/localizationImport.png)
7. Finally, you'll got localized stroyboard string file.
![ScreenShot](/docs/screenshot/localizationStroyboardFile.png)
