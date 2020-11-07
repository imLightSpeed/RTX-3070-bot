from check_stock import stock,main
import time

card_urls_bb = { '3070 Founders Edition':'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442',
                'EVGA 3070':'https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-black-gaming-8gb-gddr6x-pci-express-4-0-graphics-card/6439300.p?skuId=6439300',
                'GIGABYTE 3070':'https://www.bestbuy.com/site/gigabyte-geforce-rtx-3070-8g-gddr6-pci-express-4-0-graphics-card-black/6437909.p?skuId=6437909',
                'GIGABYTE 3070 GREY':'https://www.bestbuy.com/site/gigabyte-geforce-rtx-3070-8g-gddr6-pci-express-4-0-graphics-card-black/6437912.p?skuId=6437912',
                }

card_urls_ne = { 
                'EVGA 3070':'https://www.newegg.com/evga-geforce-rtx-3070-08g-p5-3751-kr/p/N82E16814487528?Description=3070&cm_re=3070-_-14-487-528-_-Product',
                'MSI VENTUS 3x':'https://www.newegg.com/msi-geforce-rtx-3070-rtx-3070-ventus-3x-oc/p/N82E16814137601?Description=RTX%203070&cm_re=RTX_3070-_-14-137-601-_-Product&quicklink=true',
                'MSI VENTUS 2x':'https://www.newegg.com/msi-geforce-rtx-3070-rtx-3070-ventus-2x-oc/p/N82E16814137602?Description=RTX%203070&cm_re=RTX_3070-_-14-137-602-_-Product',
                'GIGABYTE 3070':'https://www.newegg.com/gigabyte-geforce-rtx-3070-gv-n3070gaming-oc-8gd/p/N82E16814932342?Description=RTX%203070&cm_re=RTX_3070-_-14-932-342-_-Product',
                'ASUS ROG-STRIX':'https://www.newegg.com/asus-geforce-rtx-3070-rog-strix-rtx3070-o8g-gaming/p/N82E16814126458?Description=RTX%203070&cm_re=RTX_3070-_-14-126-458-_-Product',
                'MSI TRIO':'https://www.newegg.com/msi-geforce-rtx-3070-rtx-3070-gaming-x-trio/p/N82E16814137603?Description=RTX%203070&cm_re=RTX_3070-_-14-137-603-_-Product',
                'EVGA ULTRA':'https://www.newegg.com/evga-geforce-rtx-3070-08g-p5-3767-kr/p/N82E16814487532?Description=RTX%203070&cm_re=RTX_3070-_-14-487-532-_-Product',
                }
if __name__ == '__main__':
     while True:
          main(card_urls_bb, card_urls_ne)
          time.sleep(30)