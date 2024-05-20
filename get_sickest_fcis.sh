python3 get_fcis_performance_page.py | sed 's/Ver detalle//g'| sed 's/Operar//g' > page.html
python3 remove_btns.py
python3 get_performances.py | head -24 > fci_performances
python3 get_top3.py
