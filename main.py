import yaml
import abjad
try: from yaml import CSafeLoader as SafeLoader
except ImportError:
    from yaml import SafeLoader

CORE_DEFS_PATH = 'core.yaml'

DEFINITION_NUCLEUS = abjad.NamedPitch("c''")
KEY_SIGNATURE = abjad.KeySignature(abjad.NamedPitchClass('b'), abjad.Mode('major'))

INTERVAL = KEY_SIGNATURE.tonic.number - DEFINITION_NUCLEUS.pitch_class.number
while INTERVAL > 6:
    INTERVAL -= 12

def main():
    with open(CORE_DEFS_PATH) as f:
        defs = yaml.load(f.read(), SafeLoader)
    while term := input('Enter term (blank to exit): ').strip().lower():
        if term in defs:
            print('Loading... Close window to run again')
            voice = abjad.Voice(defs[term])
            abjad.mutate.transpose(voice, INTERVAL)
            staff = abjad.Staff([voice])
            abjad.attach(KEY_SIGNATURE, staff[0][0])
            abjad.show(staff)
        else:
            print(f"Unknown term '{term}'")

if __name__ == '__main__':
    main()
