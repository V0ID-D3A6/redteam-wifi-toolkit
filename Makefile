.PHONY: help wifi lan report clean

help:
	@echo "Red Team Wi-Fi Recon Toolkit"
	@echo ""
	@echo "Usage:"
	@echo "  make wifi IFACE=wlan0mon     Run Wi-Fi reconnaissance"
	@echo "  make lan IFACE=eth0          Run LAN mapping"
	@echo "  make report                  Build recon report"
	@echo "  make clean                   Remove output files"

wifi:
	sudo python3 wifi_recon.py -i $(IFACE)

lan:
	sudo python3 network_mapper.py -i $(IFACE)

report:
	python3 report_builder.py

clean:
	rm -rf output/*.json output/report.md
