from toontown.safezone.AAASafeZoneLoader import AAASafeZoneLoader
from toontown.town.AAATownLoader import AAATownLoader
from toontown.toonbase import ToontownGlobals
from toontown.hood.ToonHood import ToonHood

class AAAHood(ToonHood):
    notify = directNotify.newCategory('AAAHood')

    ID = ToontownGlobals.ArfArfAlley
    TOWNLOADER_CLASS = AAATownLoader
    SAFEZONELOADER_CLASS = AAASafeZoneLoader
    STORAGE_DNA = 'phase_8/dna/storage_DG.pdna'
    SKY_FILE = 'phase_3.5/models/props/TT_sky'
    SPOOKY_SKY_FILE = 'phase_3.5/models/props/BR_sky'
    TITLE_COLOR = (0.8, 0.6, 1.0, 1.0)

    HOLIDAY_DNA = {
      ToontownGlobals.CHRISTMAS: ['phase_8/dna/winter_storage_DG.pdna'],
      ToontownGlobals.HALLOWEEN: ['phase_8/dna/halloween_props_storage_DG.pdna']}
