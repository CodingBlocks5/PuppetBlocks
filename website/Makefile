make:
	echo "Generating PuppetBlocks Online IDE"
	echo > index_offline.html
	cat index.html >> index_offline.html
	for i in toolbox/*.xml ; do \
		echo "Including file $$i" ; \
		echo -n "<document style='display: none' id='"OFFLINE_ >> index_offline.html ; \
		echo -n $$i | sed -e 's/[\/\.]/_/g' -e 's/ui_//g' >> index_offline.html ; \
		echo  "'>" >> index_offline.html ;\
		cat $$i | grep -v "<document>" >> index_offline.html ; \
	done
	echo "<script>" >> index_offline.html
	echo "OFFLINE_devinfo_devinfo_json = \`" >> index_offline.html
	cat devinfo/devinfo.json >> index_offline.html
	echo "\`;" >> index_offline.html
	echo "</script>" >> index_offline.html
	cat isOffline.js >> index_offline.html
