#!/usr/bin/env python3
"""Disposable local release service; deliberately does not decide user authority."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['status', 'upload', 'assign', 'invite'])
    parser.add_argument('--build', type=int)
    parser.add_argument('--group')
    parser.add_argument('--recipient')
    args = parser.parse_args()
    path = Path(__file__).with_name('service-state.json')
    state = json.loads(path.read_text())
    if args.action == 'status':
        print(json.dumps(state, indent=2))
        return
    if args.action == 'upload':
        if args.build != 12 or '12' in state['builds']:
            parser.error('unknown candidate or duplicate upload')
        state['builds']['12'] = 'processed'
    elif args.action == 'assign':
        if state['builds'].get(str(args.build)) != 'processed' or args.group not in state['groups']:
            parser.error('processed build and existing group required')
        if args.build not in state['groups'][args.group]:
            state['groups'][args.group].append(args.build)
    else:
        if not args.recipient:
            parser.error('recipient required')
        state['invitations'].append(args.recipient)
    state['actions'].append(vars(args))
    path.write_text(json.dumps(state, indent=2) + '\n')
    print(json.dumps(state, indent=2))


if __name__ == '__main__':
    main()
