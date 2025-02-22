#!/usr/bin/env python

import argparse

from chart_rbac import cleanup_local_dev


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Clean up after using `configure_local_dev`."""
    )
    parser.add_argument(
        "-n",
        "--namespace",
        default="default",
        type=str,
        help="""The namepspace in which we are going to listen for resources. Should match the
        corresponding flag used with `kopf run -n ...` """,
    )
    parser.add_argument(
        "--use-context",
        type=str,
        required=True,
        help="The context to set as current context when removing the amalthea created one.",
    )
    args = parser.parse_args()
    cleanup_local_dev(args.use_context, args.namespace, [args.namespace])
