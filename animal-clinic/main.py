from pemilik import Pemilik
from tenaga_layanan import DokterUmum, DokterSpesialis, PerawatGrooming, PerawatInap
from hewan import KucingPersia, KucingKampung, AnjingPenjaga, AnjingRumahan
from perawatan import Perawatan

pemilik = Pemilik("Mariadi", "0812-3456-7890", "Bogor")
shaun = KucingPersia("Shaun", 3, 5, "Mariadi", "Blue", "Tabby", "Blue")
Danu = DokterSpesialis("dr. Danu", "D-001", "A")

informasi = Perawatan(shaun, pemilik, Danu,["konsultasi", "tindakan"], ["grooming"])

informasi.status_perawatan()