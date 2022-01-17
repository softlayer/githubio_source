let shell = require('shelljs')
const fs = require('fs')

const ROUTE_FILES = 'C:/Users/LVV941629/Forks/Edson/githubio_source/content'
const FIND_STRING_TAG = 'tags:'
const CONDITION_STR_TO_FINISH_THE_CHANGE = ['---', 'aliases:', 'author: "sldn"', 'classes:']
const IGNORE_DIRECTORIES = ['reference/', 'release_notes/']
// Codes ASCII
const CODE_LINE_BREAK = 10

let listFiles = shell.exec(
    `cd ${ROUTE_FILES} & find . -type f`
)

let arrayFilesAddress = separateByLineBreak(listFiles.stdout)
arrayFilesAddress = ignoreDirectories(IGNORE_DIRECTORIES, arrayFilesAddress)
reviewFiles(arrayFilesAddress)

function reviewFiles(arrayFilesAddress) {
    for (let index = 0; index < arrayFilesAddress.length; index++) {
        let file = fs.readFileSync(ROUTE_FILES + arrayFilesAddress[index], "utf8")
        fs.writeFileSync(ROUTE_FILES + arrayFilesAddress[index], cleanTags(file))
        console.log("File changed:", ROUTE_FILES + arrayFilesAddress[index])
    }
}

function cleanTags(file) {
    let finalString = ''
    let newOneLineString = ''
    let sw = 0
    for (let index = 0; index < file.length; index++) {
        if (file.charCodeAt(index) != CODE_LINE_BREAK) {
            newOneLineString += file.charAt(index)
        } else {
            if (newOneLineString.substring(0, newOneLineString.length - 1) == FIND_STRING_TAG) {
                sw = 1
            }
            if (verifyConditionForFinishTags(CONDITION_STR_TO_FINISH_THE_CHANGE, newOneLineString.substring(0, newOneLineString.length - 1)) && sw == 1) {
                sw = 0
            }
            if (sw == 1) {
                newOneLineString = newOneLineString.toLowerCase()
            }
            newOneLineString += file.charAt(index)
            finalString += newOneLineString
            newOneLineString = ''
        }
    }
    finalString += newOneLineString
    return finalString
}

function verifyConditionForFinishTags(conditionStrToFinishChange, stringToVerify) {
    for (let index = 0; index < conditionStrToFinishChange.length; index++) {
        if (conditionStrToFinishChange[index] == stringToVerify) {
            return true
        }
    }
    return false
}

function separateByLineBreak(bigString) {
    let oneLineString = ""
    let arrayString = []
    for (let index = 0; index < bigString.length; index++) {
        if (bigString.charCodeAt(index) != CODE_LINE_BREAK) {
            oneLineString += bigString.charAt(index)
        } else {
            arrayString.push(oneLineString.substring(1, oneLineString.length))
            oneLineString = ""
        }
    }
    return arrayString
}

function ignoreDirectories(arrayIgnoreDirectories, arrayFilesAddress) {
    let arrayDirectoriesCleaned = []
    let sw = 0
    for (let indexI = 0; indexI < arrayFilesAddress.length; indexI++) {
        for (let indexJ = 0; indexJ < arrayIgnoreDirectories.length; indexJ++) {
            if (arrayFilesAddress[indexI].indexOf(arrayIgnoreDirectories[indexJ]) >= 0) {
                sw = 1
            }
        }
        if (sw == 0) {
            arrayDirectoriesCleaned.push(arrayFilesAddress[indexI])
        }
        sw = 0
    }
    return arrayDirectoriesCleaned
}
