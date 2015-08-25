Create target localization xliff file for Xcode import.

####Dependent module

1. lxml  
If you have problem with install lxml module in Mac OS. Please trying run the commandline below:  
(Maybe needs sudo) `STATIC_DEPS=true pip install lxml`


####When you need this project
When you start a Xcode project with Storyboard for UI development and want to localize your project using single infoPlist.strings file.

####Guideline
1. Input a Key instead of a text . ex. Key "firstPg_str01" as screenshot below  
![ScreenShot](/docs/screenshot/storyboard1.png)
2. Export xliff file from your project.  
![ScreenShot](/docs/screenshot/localizationExport.png)
3. Select "Development Language Only". It will export a Base Xliff file for traslation.  
![ScreenShot](/docs/screenshot/baseLangExport.png)
4. Execute $python targetXliff.py [base_file] [source_file] [target_language]  
    ex. `$python targetXliff.py en.xliff infoPlist.plist ja`      
![ScreenShot](/docs/screenshot/localizationFile.png)  
5. After step 4. The target xliff file with target language will be created.   
    It's according to mapping the text value of note tag in en.xliff with Key in infoPlist.plist file.
6. The final step is import created Target xliff file by Xcode.
![ScreenShot](/docs/screenshot/localizationImport.png)
