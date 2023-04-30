class Illumination:
    def increase_illumination(self):
        def doKey(down):
            NSSystemDefined = 14

            DECODE_TO_INT_KEY_F6 = 21

            ev = Quartz.NSEvent.otherEventWithType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(
                NSSystemDefined,
                (0, 0),
                0xa00 if down else 0xb00,
                0,
                0,
                0,
                8,
                (DECODE_TO_INT_KEY_F6 << 16) | ((0xa if down else 0xb) << 8),
                -1
            )
            cev = ev.CGEvent()
            Quartz.CGEventPost(0, cev)

        doKey(True)
        doKey(False)

    def decrease_illumination(self):
        def doKey(down):
            # NSEvent.h
            NSSystemDefined = 14

            DECODE_TO_INT_KEY_F5 = 22

            ev = Quartz.NSEvent.otherEventthType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(
                NSSystemDefined,  # type
                (0, 0),  # location
                0xa00 if down else 0xb00,  # flags
                0,  # timestamp
                0,  # window
                0,  # ctx
                8,  # subtype
                (DECODE_TO_INT_KEY_F5 << 16) | ((0xa if down else 0xb) << 8),  # data1
                -1  # data2
            )
            cev = ev.CGEvent()
            Quartz.CGEventPost(0, cev)

        doKey(True)
        doKey(False)
