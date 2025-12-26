# SentryVault

## Overview

**SentryVault** is a local security tool designed to store sensitive information using a custom encryption method. Instead of storing plain text, the application validates a user's master key and uses it to "scramble" secrets before saving them to disk.  

This project was built to demonstrate proficiency in Test-Driven Development (TDD), Python logic, and secure data handling.

## Features

**Master Key Validation:** Ensures keys meet professional security standards (length, complexity).  
**Custom Shift Cipher:** An encryption engine that uses the master key's properties to obfuscate data.  
**Persistent Storage:** Encrypted data is saved to a local text file.  
**Decryption Engine:** Allows users to retrieve their secrets only if they provide the correct master key.  

## Technical Skills Demonstrated

**TDD (unittest):** 100% logic coverage before implementation.  
**Algorithmic Logic:** String manipulation and mathematical shifting.  
**File I/O:** Handling persistent data and "File Not Found" edge cases.  
**Separation of Concerns:** Keeping business logic separate from the user interface.  

## How to Run

Clone the repo.  
Run python3 main.py.
