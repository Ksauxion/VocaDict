function manifest()
    myManifest = {
        name = "VocaDict",
        comment = "A plugin for custon dictionaries in Vocaloid",
        author = "Ksauxion",
        pluginID = "{C2987211-451A-44CB-BE91-D6A713626A20}",
        pluginVersion = "1.0.0.0",
        apiVersion = "3.0.0.1"
    }

    return myManifest
end

function read_dict(dict_p)
    local dic = io.open(dict_p)
    dic = dic:lines()
    dict = {}
    for line in dic do
        table.insert(dict, line)
    end
    local whole_w = {}
    local parts = {}
    local phones = {}
    local vowels = {}

    for w in string.gmatch(dict[1], "([^,]+)") do
        table.insert(vowels, w)
    end

    for i = 2, #dict do
        local a = {}
        for w in string.gmatch(dict[i], "([^,]+)") do
            table.insert(a, w)
        end
        dict[i] = a
    end

    for i = 2, #dict do
        local a = {}
        for w in string.gmatch(dict[i][2], "([^-]+)") do
            table.insert(a, w)
        end
        dict[i][2] = a
        for j = 1, #dict[i][2] - 1 do
            dict[i][2][j] = dict[i][2][j] .. "-"
        end

        local a = {}
        for w in string.gmatch(dict[i][3], "([^-]+)") do
            table.insert(a, w)
        end
        dict[i][3] = a
    end
    for gh = 1, #dict do
        table.insert(whole_w, dict[gh][1])
        table.insert(parts, dict[gh][2])
        table.insert(phones, dict[gh][3])
    end
    return whole_w, parts, phones, vowels
end

function load_cfg()
    local d = io.open("settings.txt")
    local d = d:lines()
    ff = {}
    for line in d do
        table.insert(ff, line)
    end
    return ff[1]
end

function bin_search(item, list)
    fl = 1
    ceiling = #list

    while fl <= ceiling do
        mid = math.floor((fl + ceiling) / 2)
        tr = list[mid]
        if tr == item then
            return mid
        elseif tr > item then
            ceiling = mid - 1
        else
            fl = mid + 1
        end
    end
    return 0
end

function main(processParam, envParam)
    local path_t_d = load_cfg()

    whole_w, parts, phones, vowels = read_dict(path_t_d)

    local noteEx = {}
    local noteExList = {}
    local noteCount
    local retCode
    local idx

    VSSeekToBeginNote()
    idx = 1
    retCode, noteEx = VSGetNextNoteEx()
    while (retCode == 1) do
        noteExList[idx] = noteEx
        retCode, noteEx = VSGetNextNoteEx()
        idx = idx + 1
    end

    noteCount = table.getn(noteExList)
    if (noteCount == 0) then
        VSMessageBox("No notes loaded.", 0)
        return 0
    end

    for idx = 1, noteCount do
        local updNoteEx = {}
        updNoteEx = noteExList[idx]
        noteExList[idx].lyric = noteExList[idx].lyric:gsub("|", "")
        idj = bin_search(noteExList[idx].lyric, whole_w)
        if idj > 0 then
            updNoteEx.lyric = parts[idj][1]
            updNoteEx.phonemes = phones[idj][1]
            updNoteEx.phLock = 1

            for idk = 2, #parts[idj] do
                if noteExList[idx + idk - 1].lyric == "+" then
                    noteExList[idx + idk - 1].lyric = parts[idj][idk]
                    noteExList[idx + idk - 1].phonemes = phones[idj][idk]
                else
                    break
                end
            end
        end

        retCode = VSUpdateNoteEx(updNoteEx)
        if (retCode ~= 1) then
            VSMessageBox("Failed to update note!", 0)
            return 1
        end
    end

    return 0
end
