from colorama import init, Fore, Back, Style

#Initialize colorama for cross-platform colored terminal output
init()

#Print colored Hello world
print(f"{Fore.RED}{Back.YELLOW}Hello world!{Style.RESET_ALL}")
print(f"{Fore.GREEN}Hello world in Green!{Style.RESET_ALL}")
print(f"{Fore.BLUE}{Style.BRIGHT}Hello world in Bright Blue!{Style.RESET_ALL}")
print(f"{Fore.MAGENTA}{Back.CYAN}Hello world with Magenta text and Cyan background!{Style.RESET_ALL}")