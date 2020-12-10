from advent import AdventAPI


class State():
    def __init__(self, acc: int = 0, pos: int = 0,
        operation: str = 'init', before = None):
        self.acc = acc
        self.pos = pos
        self.operation = operation
        self.before = before

    def accumulate(self, value: int):
        return State(
            acc=self.acc + value,
            pos=self.pos + 1,
            operation='acc',
            before=self
        )

    def jump(self, value: int):
        return State(
            acc=self.acc,
            pos=self.pos + value,
            operation='jmp',
            before=self
        )
    
    def nop(self):
        return State(
            acc=self.acc,
            pos=self.pos + 1,
            operation='nop',
            before=self
        )
    

    def __eq__(self, state) -> bool:
        return self.pos == state.pos

    def list(self):
        if not self.before:
            return [self]
        else:
            return self.before.list() + [self]

    def isLoop(self) -> bool:
        states = [
            state
            for state in self.before.list()
            if state == self
        ]
        return len(states) > 0

    def get_last_jump_or_nop(self):
        if not self.before:
            return False
        elif self.operation in ['jmp', 'nop']:
            return self.before
        else:
            return self.before.get_last_jump_or_nop()

    def __repr__(self) -> str:
        return 'pos:{} acc:{} last_op: {}'.format(self.pos, self.acc, self.operation)


class Computer():
    def __init__(self, instr_list: list[str]):
        self.instr_list = instr_list

    def run(self, state: State = State()) -> int:
        if state.pos in range(len(self.instr_list)):
            instr = self.instr_list[state.pos]
        else:
            return (True, state)

        if instr.startswith('acc'):
            new_state = state.accumulate(int(instr[4:]))
        elif instr.startswith('nop'):
            new_state = state.nop()
        elif instr.startswith('jmp'):
            new_state = state.jump(int(instr[4:]))

        if new_state.isLoop():
            return (False, state)
        else:
            return self.run(new_state)

    def repair(self, state) -> State:
        last = state.get_last_jump_or_nop()
        if not last:
            print(state)
            return False
        instr = self.instr_list[last.pos]
        
        if instr.startswith('jmp'):
            new_state = last.nop()
        else:
            new_state = last.jump(int(instr[4:]))
        
        terminates, state = self.run(new_state)

        if terminates:
            return state
        else:
            return self.repair(last)




a = AdventAPI()

inp = a.get_input(8).decode().splitlines()

c = Computer(inp)

terminates, state = c.run()
print(state)
print(c.repair(state))