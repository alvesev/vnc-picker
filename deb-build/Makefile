DIR_ORIGIN_SRC = ../src
DIR_ORIGIN_DOC = ../doc

all: install

install:
	PS4="CMD:\${0}:pid=\${$}: "
	set -x
	test -d $(DESTDIR)/opt/vnc-picker/ || install --directory --owner=root --group=root --mode=755 --verbose $(DESTDIR)/opt/vnc-picker/
	install --owner=root --group=root --mode=755 --verbose $(DIR_ORIGIN_SRC)/vnc-picker $(DESTDIR)/opt/vnc-picker/vnc-picker
	install --owner=root --group=root --mode=755 --verbose $(DIR_ORIGIN_SRC)/print-nodes-confs.py $(DESTDIR)/opt/vnc-picker/print-nodes-confs.py
	install --owner=root --group=root --mode=644 --verbose $(DIR_ORIGIN_SRC)/vnc-picker.conf $(DESTDIR)/opt/vnc-picker/vnc-picker.conf
	install --owner=root --group=root --mode=644 --verbose $(DIR_ORIGIN_SRC)/xstartup $(DESTDIR)/opt/vnc-picker/xstartup

	install --directory --owner=root --group=root --mode=755 --verbose $(DESTDIR)/opt/vnc-picker/doc
	cp --recursive $(DIR_ORIGIN_DOC)/* $(DESTDIR)/opt/vnc-picker/doc
	chown -R root.root $(DESTDIR)/opt/vnc-picker/doc
	find $(DESTDIR)/opt/vnc-picker/doc -type d -exec chmod 755 '{}' \;
	find $(DESTDIR)/opt/vnc-picker/doc -type f -exec chmod 644 '{}' \;
	
	install --directory --owner=root --group=root --mode=755 --verbose $(DESTDIR)/opt/vnc-picker/devilspie-configuration
	install --owner=root --group=root --mode=644 --verbose $(DIR_ORIGIN_SRC)/devilspie-configuration/* $(DESTDIR)/opt/vnc-picker/devilspie-configuration

	install --directory --owner=root --group=root --mode=755 --verbose $(DESTDIR)/opt/vnc-picker/fonts-configuration
	install --owner=root --group=root --mode=644 --verbose $(DIR_ORIGIN_SRC)/fonts-configuration/* $(DESTDIR)/opt/vnc-picker/fonts-configuration

clean:
	echo "INFO:${0}:pid=${$}: Nothing to be done for cleanup after this DEB package build."
