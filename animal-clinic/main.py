from hewan import KucingPersia
from layanan import Layanan

sheep = KucingPersia("sheep", 3, 5, "Mariadi", "Blue", "Tabby", "Blue")
service = Layanan()

total = service.total_tagihan(sheep, ["grooming", "inap", "perawatan_bulu"])
print(f"Total akhir: Rp{total:,}")