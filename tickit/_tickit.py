from ctypes import *

STRING = c_char_p


TICKIT_N_PEN_ATTRS = 8
TICKIT_PEN_ALTFONT = 7
TICKIT_PEN_STRIKE = 6
TICKIT_PEN_REVERSE = 5
TICKIT_PEN_ITALIC = 4
TICKIT_PEN_UNDER = 3
TICKIT_PEN_BG = 1
TICKIT_PEN_FG = 0
TICKIT_EV_UNBIND = -2147483648
TICKIT_EV_CHANGE = 8
TICKIT_EV_MOUSE = 4
TICKIT_PENTYPE_COLOUR = 2
TICKIT_EV_KEY = 2
TICKIT_PENTYPE_INT = 1
TICKIT_PENTYPE_BOOL = 0
TICKIT_EV_RESIZE = 1
TICKIT_MOUSEWHEEL_DOWN = 2
TICKIT_MOUSEWHEEL_UP = 1
TICKIT_MOUSEEV_WHEEL = 4
TICKIT_MOUSEEV_RELEASE = 3
TICKIT_MOUSEEV_DRAG = 2
TICKIT_MOUSEEV_PRESS = 1
TICKIT_TERM_CURSORSHAPE_BLOCK = 1
TICKIT_TERM_CURSORSHAPE_LEFT_BAR = 3
TICKIT_TERM_CURSORSHAPE_UNDER = 2
TICKIT_TERMCTL_ICONTITLE_TEXT = 8
TICKIT_TERMCTL_TITLE_TEXT = 7
TICKIT_TERMCTL_ICON_TEXT = 6
TICKIT_TERMCTL_CURSORSHAPE = 5
TICKIT_TERMCTL_CURSORBLINK = 4
TICKIT_TERMCTL_CURSORVIS = 2
TICKIT_TERMCTL_ALTSCREEN = 1
TICKIT_PEN_BOLD = 2
TICKIT_TERMCTL_KEYPAD_APP = 9
TICKIT_KEYEV_TEXT = 2
TICKIT_KEYEV_KEY = 1
TICKIT_TERMCTL_MOUSE = 3
class div_t(Structure):
    pass
div_t._fields_ = [
    ('quot', c_int),
    ('rem', c_int),
]
class ldiv_t(Structure):
    pass
ldiv_t._fields_ = [
    ('quot', c_long),
    ('rem', c_long),
]
class lldiv_t(Structure):
    pass
lldiv_t._fields_ = [
    ('quot', c_longlong),
    ('rem', c_longlong),
]
class random_data(Structure):
    pass
int32_t = c_int32
random_data._fields_ = [
    ('fptr', POINTER(int32_t)),
    ('rptr', POINTER(int32_t)),
    ('state', POINTER(int32_t)),
    ('rand_type', c_int),
    ('rand_deg', c_int),
    ('rand_sep', c_int),
    ('end_ptr', POINTER(int32_t)),
]
class drand48_data(Structure):
    pass
drand48_data._fields_ = [
    ('__x', c_ushort * 3),
    ('__old_x', c_ushort * 3),
    ('__c', c_ushort),
    ('__init', c_ushort),
    ('__a', c_ulonglong),
]
__compar_fn_t = CFUNCTYPE(c_int, c_void_p, c_void_p)
comparison_fn_t = __compar_fn_t
__compar_d_fn_t = CFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)
__clock_t = c_long
clock_t = __clock_t
__time_t = c_long
time_t = __time_t
__clockid_t = c_int
clockid_t = __clockid_t
__timer_t = c_void_p
timer_t = __timer_t
class timespec(Structure):
    pass
timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', c_long),
]
pthread_t = c_ulong
class pthread_attr_t(Union):
    pass
pthread_attr_t._fields_ = [
    ('__size', c_char * 56),
    ('__align', c_long),
]
class __pthread_internal_list(Structure):
    pass
__pthread_internal_list._fields_ = [
    ('__prev', POINTER(__pthread_internal_list)),
    ('__next', POINTER(__pthread_internal_list)),
]
__pthread_list_t = __pthread_internal_list
class __pthread_mutex_s(Structure):
    pass
__pthread_mutex_s._fields_ = [
    ('__lock', c_int),
    ('__count', c_uint),
    ('__owner', c_int),
    ('__nusers', c_uint),
    ('__kind', c_int),
    ('__spins', c_int),
    ('__list', __pthread_list_t),
]
class pthread_mutex_t(Union):
    pass
pthread_mutex_t._fields_ = [
    ('__data', __pthread_mutex_s),
    ('__size', c_char * 40),
    ('__align', c_long),
]
class pthread_mutexattr_t(Union):
    pass
pthread_mutexattr_t._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]
class N14pthread_cond_t4DOT_12E(Structure):
    pass
N14pthread_cond_t4DOT_12E._fields_ = [
    ('__lock', c_int),
    ('__futex', c_uint),
    ('__total_seq', c_ulonglong),
    ('__wakeup_seq', c_ulonglong),
    ('__woken_seq', c_ulonglong),
    ('__mutex', c_void_p),
    ('__nwaiters', c_uint),
    ('__broadcast_seq', c_uint),
]
class pthread_cond_t(Union):
    pass
pthread_cond_t._fields_ = [
    ('__data', N14pthread_cond_t4DOT_12E),
    ('__size', c_char * 48),
    ('__align', c_longlong),
]
class pthread_condattr_t(Union):
    pass
pthread_condattr_t._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]
pthread_key_t = c_uint
pthread_once_t = c_int
class N16pthread_rwlock_t4DOT_15E(Structure):
    pass
N16pthread_rwlock_t4DOT_15E._fields_ = [
    ('__lock', c_int),
    ('__nr_readers', c_uint),
    ('__readers_wakeup', c_uint),
    ('__writer_wakeup', c_uint),
    ('__nr_readers_queued', c_uint),
    ('__nr_writers_queued', c_uint),
    ('__writer', c_int),
    ('__shared', c_int),
    ('__pad1', c_ulong),
    ('__pad2', c_ulong),
    ('__flags', c_uint),
]
class pthread_rwlock_t(Union):
    pass
pthread_rwlock_t._fields_ = [
    ('__data', N16pthread_rwlock_t4DOT_15E),
    ('__size', c_char * 56),
    ('__align', c_long),
]
class pthread_rwlockattr_t(Union):
    pass
pthread_rwlockattr_t._fields_ = [
    ('__size', c_char * 8),
    ('__align', c_long),
]
pthread_spinlock_t = c_int
class pthread_barrier_t(Union):
    pass
pthread_barrier_t._fields_ = [
    ('__size', c_char * 32),
    ('__align', c_long),
]
class pthread_barrierattr_t(Union):
    pass
pthread_barrierattr_t._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]
__sig_atomic_t = c_int
class __sigset_t(Structure):
    pass
__sigset_t._fields_ = [
    ('__val', c_ulong * 16),
]
class timeval(Structure):
    pass
__suseconds_t = c_long
timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]
__u_char = c_ubyte
__u_short = c_ushort
__u_int = c_uint
__u_long = c_ulong
__int8_t = c_byte
__uint8_t = c_ubyte
__int16_t = c_short
__uint16_t = c_ushort
__int32_t = c_int
__uint32_t = c_uint
__int64_t = c_long
__uint64_t = c_ulong
__quad_t = c_long
__u_quad_t = c_ulong
__dev_t = c_ulong
__uid_t = c_uint
__gid_t = c_uint
__ino_t = c_ulong
__ino64_t = c_ulong
__mode_t = c_uint
__nlink_t = c_ulong
__off_t = c_long
__off64_t = c_long
__pid_t = c_int
class __fsid_t(Structure):
    pass
__fsid_t._fields_ = [
    ('__val', c_int * 2),
]
__rlim_t = c_ulong
__rlim64_t = c_ulong
__id_t = c_uint
__useconds_t = c_uint
__daddr_t = c_int
__swblk_t = c_long
__key_t = c_int
__blksize_t = c_long
__blkcnt_t = c_long
__blkcnt64_t = c_long
__fsblkcnt_t = c_ulong
__fsblkcnt64_t = c_ulong
__fsfilcnt_t = c_ulong
__fsfilcnt64_t = c_ulong
__ssize_t = c_long
__loff_t = __off64_t
__qaddr_t = POINTER(__quad_t)
__caddr_t = STRING
__intptr_t = c_long
__socklen_t = c_uint
class wait(Union):
    pass
class N4wait3DOT_0E(Structure):
    pass
N4wait3DOT_0E._fields_ = [
    ('__w_termsig', c_uint, 7),
    ('__w_coredump', c_uint, 1),
    ('__w_retcode', c_uint, 8),
    ('', c_uint, 16),
]
class N4wait3DOT_1E(Structure):
    pass
N4wait3DOT_1E._fields_ = [
    ('__w_stopval', c_uint, 8),
    ('__w_stopsig', c_uint, 8),
    ('', c_uint, 16),
]
wait._fields_ = [
    ('w_status', c_int),
    ('__wait_terminated', N4wait3DOT_0E),
    ('__wait_stopped', N4wait3DOT_1E),
]
sigset_t = __sigset_t
__fd_mask = c_long
class fd_set(Structure):
    pass
fd_set._fields_ = [
    ('fds_bits', __fd_mask * 16),
]
fd_mask = __fd_mask
u_char = __u_char
u_short = __u_short
u_int = __u_int
u_long = __u_long
quad_t = __quad_t
u_quad_t = __u_quad_t
fsid_t = __fsid_t
loff_t = __loff_t
ino_t = __ino_t
ino64_t = __ino64_t
dev_t = __dev_t
gid_t = __gid_t
mode_t = __mode_t
nlink_t = __nlink_t
uid_t = __uid_t
off_t = __off_t
off64_t = __off64_t
pid_t = __pid_t
id_t = __id_t
ssize_t = __ssize_t
daddr_t = __daddr_t
caddr_t = __caddr_t
key_t = __key_t
useconds_t = __useconds_t
suseconds_t = __suseconds_t
ulong = c_ulong
ushort = c_ushort
uint = c_uint
int8_t = c_int8
int16_t = c_int16
int64_t = c_int64
u_int8_t = c_ubyte
u_int16_t = c_ushort
u_int32_t = c_uint
u_int64_t = c_ulong
register_t = c_long
blksize_t = __blksize_t
blkcnt_t = __blkcnt_t
fsblkcnt_t = __fsblkcnt_t
fsfilcnt_t = __fsfilcnt_t
blkcnt64_t = __blkcnt64_t
fsblkcnt64_t = __fsblkcnt64_t
fsfilcnt64_t = __fsfilcnt64_t
class __locale_struct(Structure):
    pass
class __locale_data(Structure):
    pass
__locale_struct._fields_ = [
    ('__locales', POINTER(__locale_data) * 13),
    ('__ctype_b', POINTER(c_ushort)),
    ('__ctype_tolower', POINTER(c_int)),
    ('__ctype_toupper', POINTER(c_int)),
    ('__names', STRING * 13),
]
__locale_data._fields_ = [
]
__locale_t = POINTER(__locale_struct)
locale_t = __locale_t
size_t = c_ulong

# values for enumeration 'TickitEventType'
TickitEventType = c_int # enum

# values for enumeration 'TickitKeyEventType'
TickitKeyEventType = c_int # enum

# values for enumeration 'TickitMouseEventType'
TickitMouseEventType = c_int # enum

# values for unnamed enumeration
class TickitEvent(Structure):
    pass
TickitEvent._fields_ = [
    ('lines', c_int),
    ('cols', c_int),
    ('type', c_int),
    ('str', STRING),
    ('button', c_int),
    ('line', c_int),
    ('col', c_int),
]
class TickitPen(Structure):
    pass
TickitPen._fields_ = [
]

# values for enumeration 'TickitPenAttr'
TickitPenAttr = c_int # enum

# values for enumeration 'TickitPenAttrType'
TickitPenAttrType = c_int # enum
TickitPenEventFn = CFUNCTYPE(None, POINTER(TickitPen), TickitEventType, POINTER(TickitEvent), c_void_p)
class TickitTerm(Structure):
    pass
TickitTerm._fields_ = [
]
TickitTermOutputFunc = CFUNCTYPE(None, POINTER(TickitTerm), STRING, size_t, c_void_p)
TickitTermEventFn = CFUNCTYPE(None, POINTER(TickitTerm), TickitEventType, POINTER(TickitEvent), c_void_p)

# values for enumeration 'TickitTermCtl'
TickitTermCtl = c_int # enum

# values for enumeration 'TickitTermCursorShape'
TickitTermCursorShape = c_int # enum
class TickitStringPos(Structure):
    pass
TickitStringPos._fields_ = [
    ('bytes', size_t),
    ('codepoints', c_int),
    ('graphemes', c_int),
    ('columns', c_int),
]
__all__ = ['__uint16_t', '__pthread_mutex_s', '__int16_t',
           'TickitEvent', 'TICKIT_PEN_STRIKE', 'pthread_condattr_t',
           'pthread_once_t', 'fsfilcnt_t', '__timer_t', 'mode_t',
           'TICKIT_TERM_CURSORSHAPE_UNDER', 'size_t', 'random_data',
           'TICKIT_TERMCTL_KEYPAD_APP', '__uint32_t', 'fd_set',
           'uint', 'TICKIT_KEYEV_KEY', 'blkcnt_t', 'TICKIT_PEN_UNDER',
           '__ino64_t', 'fsblkcnt64_t', '__qaddr_t', '__mode_t',
           'TickitPenAttrType', '__loff_t', 'blksize_t',
           'TICKIT_PEN_BG', 'daddr_t', '__locale_data', 'u_char',
           'TICKIT_N_PEN_ATTRS', 'uid_t', 'TICKIT_TERMCTL_CURSORVIS',
           'u_int16_t', '__time_t', 'sigset_t', 'TickitPenEventFn',
           '__int32_t', 'pthread_rwlock_t', '__nlink_t',
           '__compar_fn_t', '__off_t', '__fsid_t', '__uint64_t',
           'timespec', 'TICKIT_EV_CHANGE', 'comparison_fn_t',
           'pthread_mutexattr_t', '__fd_mask', 'TickitPenAttr',
           'int16_t', 'TICKIT_PEN_ALTFONT', 'TickitEventType',
           'clock_t', 'TICKIT_TERMCTL_ICON_TEXT', '__sigset_t',
           '__clockid_t', '__useconds_t', 'div_t',
           'TickitTermOutputFunc', 'TickitTermEventFn', 'id_t',
           '__off64_t', 'ldiv_t', 'pthread_barrier_t',
           'N16pthread_rwlock_t4DOT_15E', 'u_int32_t', 'fd_mask',
           '__pthread_internal_list', 'TickitPen', 'TICKIT_EV_RESIZE',
           'TICKIT_MOUSEEV_RELEASE', '__intptr_t', '__u_long', 'wait',
           'ushort', 'TICKIT_MOUSEWHEEL_DOWN', '__blkcnt_t',
           '__pthread_list_t', 'clockid_t', 'pthread_attr_t',
           'caddr_t', '__ino_t', '__rlim64_t', 'ino_t',
           'TICKIT_EV_MOUSE', 'int32_t', 'off64_t',
           'TICKIT_TERMCTL_ALTSCREEN', 'TICKIT_TERMCTL_CURSORSHAPE',
           '__caddr_t', '__blksize_t', 'pthread_spinlock_t',
           'TICKIT_EV_KEY', 'TICKIT_MOUSEEV_PRESS', 'fsblkcnt_t',
           'N14pthread_cond_t4DOT_12E', 'u_quad_t', '__ssize_t',
           'register_t', 'TICKIT_TERMCTL_CURSORBLINK',
           '__compar_d_fn_t', 'N4wait3DOT_0E', 'fsfilcnt64_t',
           '__locale_struct', 'u_int64_t', '__daddr_t', 'ino64_t',
           'TICKIT_EV_UNBIND', '__sig_atomic_t',
           'TICKIT_PENTYPE_COLOUR', 'TICKIT_MOUSEEV_WHEEL',
           'TICKIT_KEYEV_TEXT', '__uint8_t', 'TickitMouseEventType',
           'TICKIT_PENTYPE_INT', '__u_char', 'TICKIT_PEN_FG',
           '__fsblkcnt64_t', 'TickitKeyEventType', 'u_int',
           'TICKIT_MOUSEWHEEL_UP', 'TICKIT_TERM_CURSORSHAPE_LEFT_BAR',
           '__blkcnt64_t', '__dev_t', 'gid_t',
           'pthread_barrierattr_t', '__suseconds_t', 'pid_t',
           'timer_t', 'quad_t', 'TickitTermCursorShape', 'u_long',
           '__fsfilcnt64_t', 'TICKIT_MOUSEEV_DRAG',
           'TICKIT_TERMCTL_TITLE_TEXT', 'pthread_key_t',
           'TickitTermCtl', 'blkcnt64_t', 'u_int8_t', 'loff_t',
           'pthread_cond_t', 'TICKIT_TERM_CURSORSHAPE_BLOCK', 'off_t',
           'TICKIT_PEN_ITALIC', 'int64_t', '__fsblkcnt_t', '__rlim_t',
           'N4wait3DOT_1E', 'time_t', 'pthread_t', '__locale_t',
           'drand48_data', 'lldiv_t', 'TickitStringPos', '__quad_t',
           'timeval', '__u_quad_t', '__u_short', '__int8_t', '__id_t',
           '__gid_t', 'fsid_t', '__pid_t', 'ulong', 'u_short',
           'TICKIT_PEN_REVERSE', 'key_t', 'TICKIT_TERMCTL_MOUSE',
           'TICKIT_PEN_BOLD', 'useconds_t', 'nlink_t',
           'pthread_rwlockattr_t', '__swblk_t', 'locale_t', 'int8_t',
           '__socklen_t', 'TICKIT_PENTYPE_BOOL', '__u_int',
           'suseconds_t', 'pthread_mutex_t', '__int64_t',
           'TickitTerm', '__key_t', 'ssize_t', '__clock_t', 'dev_t',
           '__uid_t', '__fsfilcnt_t', 'TICKIT_TERMCTL_ICONTITLE_TEXT']
