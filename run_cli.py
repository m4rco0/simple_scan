import sys
from src.interface.cli import main 


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Interrompido pelo usuario!")
        sys.exit(0)
