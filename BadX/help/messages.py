class helpMessages:
    start = """
**Help menu of BadX**

__Your Command handler -__ `{0}`

**- Updates: @{1}
- Support: @{2}**
    """

    basic = """
**Basic Commands of BadX**

 1) `{0}ping` - __to check ping.__
 2) `{0}alive` - __to check is BadX is alive.__
 3) `{0}reboot`- __to reboot/restart all BadX clients.__
 4) `{0}stats` - __to check client stats.__
 5) `{0}eval` - __to run eval/python code (only for Owner & devs).__


**For more info join @{1} & ask!**
    """

    spam = """
**Spam Commands of BadX**

 1) `{0}spam` (counts) (spam message or reply to message/media) - __to start normal spam.__
 2) `{0}delayspam` | `{0}dpsam` (delay in secs.) (counts) (spam message or reply to message/media) - __to start delay spam.__
 3) `{0}futurespam` | `{0}timespam` (time [s: second, m: minitue, h: hour, d: day]) (counts) (spam message or reply to message/media) - __to start future/time spam.__
 4) `{0}pornspam` | `{0}pspam` (counts) - __to start porn spam.__
 5) `{0}unlimitedspam` | `{0}uspam` (spam message or reply to message/media) - __to start unlimited spam.__
 6) `{0}inlimespam` | `{0}ispam` (counts) (user ID or username) (spam message or reply to message/media __[optional]__) - __to start Inline spam on specific user.__
 7) `{0}commonspam` | `{0}cspam` (counts) (user ID or username) (spam message or reply to message/media) - __to start spam in all common groups.__ 
 8) `{0}stop` - __to stop unlimited spam.__


**#NOTE: No one can spam in Restriced group. except Owner! & for more info join @{1} & ask!**
    """

    profile = """
**Profile Commands of BadX**

 1) `{0}setpic` | `{0}updatepic `(reply to media) - __to update profile pic.__
 2) `{0}setname` | `{0}updatename` (new name) - __to update profile name.__
 3) `{0}setbio` | `{0}updatebio` (new bio) - __to update profile bio.__
 4) `{0}setall` | `{0}updateall` (new name) - __using this command BadX will update name of users in sequence. [e.g #1 BadX]__


**For more info join @{1} & ask!**
    """

    raid = """
**Raid Commands of BadX**

 1) `{0}raid` (counts) (user ID/username or reply to user) - __to start raid on specific user.__
 2) `{0}multiraid` | `{0}mraid` (counts) (user ID/usernames of raid user space by space) - __to start raid on multiple users.__
 3) `{0}replyraid` | `{0}rraid` (user ID/username or reply to user) (`enable`/`disable` __[optional]__) - __to enable/disable reply raid on user.__
 4) `{0}areplyraid` | `{0}arraid` (user ID/username or reply to user) - __to enable replyraid on user.__
 5) `{0}dreplyraid` | `{0}drraid` (user ID/username or reply to user) - __to disable replyraid from user.__


**#NOTE: Owner can enable raids on anyone (including sudos) & sudo with high rank can enable raid on lower rank sudos & for more info join @{1} & ask!**
    """

    direct_message = """
**Direct Message (DM) Commands of BadX**

 1) `{0}dm` | `{0}message` (user ID/username) (message or reply to message/media) - __to send personal message to user.__
 2) `{0}dmspam` (counts) (user ID/username) (spam message or reply to message/media) - __to start personal message spam on user.__
 3) `{0}dmraid` (counts) (user ID/username or reply to user's message) - __to start personal message raid on user.__


**#NOTE: Owner can active this task on anyone (including sudos) & sudo with high rank active this task on lower rank sudos & for more info join @{1} & ask!**
    """

    extra = """
*Extra Commands of BadX**

 1) `{0}echo` | `{0}repeat`(message or reply to message/media) - __to repeat message for fun.__
 2) `{0}broadcast` | `{0}gcast` (message or reply to message/media)- __to global cast, add `copy` to cast message as it is without forward [only in reply message].__
 3) `{0}limit` - __to check is ID is limit or not!__
 4) `{0}join` (chat username/link) - __to join grpup with selected IDs.__
 5) `{0}leave` (chat username/ID)[optional] - __to leave group with selected IDs.__ 


**For more info join @{1} & ask!**
    """
