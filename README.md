# Project for Programming Techniques

## Requirements

## Project: refactoring test
You came for a job interview, and it is requested to you to look at the following code, and to refactor it.
It concerns the `UserService` class and more specifically its `AddUser` method.
We assume the code is sound in terms of business logic...
So you only have to focus on applying clean code principles.  

### Limitation:
- The `Program` class shall **not change at all**. 
 This includes `import` statements, any character modification is forbidden.
You should assume this is part of a greater system and any **non-backwards compatible change will break the system**.
Any change in that class will result in you instantly failing the exercise...
-  You can change anything in the `LegacyApp` project except for the `UserDataAccess` class and its `AddUser` method that **should stay static and with the same parameters**. But, you may (should ?) change the code of the `AddUser` method (not its prototype, but is coding).
- The module `DB` cannot change, it is given for compatibility with the real database module. You should assume it is automatically generated for instance. So, **do not modify anything into `DB` module**. 

## Expectations
So, many things cannot be change... What can you do? 
- You should modify anything into the `LegacyApp` module (excepting things that may change the `Program.py` file).
- You should add tests into `LegacyApp` to verify you are breaking the things. 
- Tests should be robust (working today, and in ten years, and in one thousand years...).
- The refactoring should be done according to Lecture 1 to 4... actually, mainly to the last one!

### Strategy
To work more efficiently, you may follow these steps:
- Add the missing unit testing! For that you should transform the code mainly apply DIP.
- Refactor the program (where you are granted to) using SOLID principles.
- Add DRY (if needed) and KISS... 

## Set up

```bash
git clone https://github.com/truonghm/pi_project.git
cd pi_project
```

- Python version: 3.9

```bash
conda create --name py39 python=3.9.7
```

- Install requirements:

```bash
pip install -r requirements.txt
```

## Checking

### Typing

```bash
mypy LegacyApp/
```

### Unit tests

```bash
python -m unittest discorver -s tests
```
