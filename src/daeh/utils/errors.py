class DaehError(Exception):
    """الخطأ الأساسي"""
    pass

class PackageNotFoundError(DaehError):
    """الحزمة غير موجودة"""
    pass

class InstallationError(DaehError):
    """فشل التثبيت"""
    pass
