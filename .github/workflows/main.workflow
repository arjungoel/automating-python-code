workflow "PR Checklist" {
  on = "pull_request"
  resolves = ["Create PR Comment"]
}

action {
  uses = "./"
  secrets = ["GH_TOKEN"]
}